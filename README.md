# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_12:05:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,406 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 12:05:16 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-27 12:04:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:03:44 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 12:03:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 12:03:43 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 12:03:40 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:03:37 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 12:03:36 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-04-27 12:03:22 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:03:12 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:03:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-27 12:03:02 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:50 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-27 12:02:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:28 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-27 12:02:26 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:13 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 12:02:11 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-27 12:02:11 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-04-27 12:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 12:01:46 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:18 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:07 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:01:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:05 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.041 |  |
| 2026-04-27 12:00:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-27 12:00:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:33:52 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 11:24:23 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:17:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:16:50 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.183 |  |
| 2026-04-27 11:15:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 11:10:19 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-27 12:03:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-27 12:00:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-27 12:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 12:03:43 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 12:03:37 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 12:02:13 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 12:02:11 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 11:33:52 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 12:03:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 12:03:44 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 12:00:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:26 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:03:02 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:04:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:03:40 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:18 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:46 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:50 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-27 12:02:11 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-27 11:15:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.016 |  |
| 2026-04-27 12:05:16 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-27 11:03:16 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.020 |  |
| 2026-04-27 12:02:28 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-27 12:03:36 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-04-27 12:03:12 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:03:22 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:01:07 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.030 |  |
| 2026-04-27 11:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-04-27 12:01:05 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.041 |  |
| 2026-04-27 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-04-27 11:07:01 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.074 |  |
| 2026-04-27 11:09:48 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.088 |  |
| 2026-04-27 11:16:50 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
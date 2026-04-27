# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_11:04:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 11:04:36 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-04-27 11:04:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-27 11:04:02 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-27 11:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-04-27 11:03:33 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-04-27 11:03:32 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-27 11:03:25 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-27 11:03:16 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.020 |  |
| 2026-04-27 11:03:01 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 11:02:43 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-04-27 11:02:39 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 11:02:26 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.058 |  |
| 2026-04-27 11:02:25 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.061 |  |
| 2026-04-27 11:02:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.060 |  |
| 2026-04-27 11:01:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:01:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.024 |  |
| 2026-04-27 11:01:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-04-27 11:01:09 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:00:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 10:32:26 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-27 10:14:04 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-27 10:12:44 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 11:04:36 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-04-27 11:04:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-27 10:07:41 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-27 11:02:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 11:03:01 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 10:02:52 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 11:02:39 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 11:00:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 10:03:40 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 10:09:00 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-27 10:32:26 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-27 10:02:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 11:01:09 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:01:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 11:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 10:01:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 10:02:35 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 10:01:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 10:01:55 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 10:14:04 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-27 11:03:25 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-27 10:01:30 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-27 10:01:02 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-27 11:03:33 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-04-27 11:04:02 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-27 11:03:16 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.020 |  |
| 2026-04-27 11:01:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-04-27 11:01:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.024 |  |
| 2026-04-27 11:03:32 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-27 11:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-04-27 10:00:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.034 |  |
| 2026-04-27 11:02:43 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-04-27 11:02:26 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.058 |  |
| 2026-04-27 10:02:32 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.059 |  |
| 2026-04-27 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.060 |  |
| 2026-04-27 11:02:25 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.061 |  |
| 2026-04-27 10:10:24 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.088 |  |
| 2026-04-27 10:01:29 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.113 |  |
| 2026-04-27 10:04:37 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
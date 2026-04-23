# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_12:29:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 12:29:43 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-23 12:12:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2026-04-23 12:10:03 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.066 |  |
| 2026-04-23 12:07:49 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-04-23 12:07:29 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:06:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:06:10 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:06:02 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-23 12:05:48 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:05:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:05:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:04:49 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:04:24 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.043 |  |
| 2026-04-23 12:04:14 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:04:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:03:45 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 12:03:17 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:03:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-04-23 12:03:16 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 12:03:13 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:03:10 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.060 |  |
| 2026-04-23 12:03:08 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-04-23 12:03:07 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-23 12:02:59 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-23 12:02:41 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.054 |  |
| 2026-04-23 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:02:19 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2026-04-23 12:02:09 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:02:08 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:02:06 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.150 |  |
| 2026-04-23 12:02:01 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.059 |  |
| 2026-04-23 12:01:50 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:01:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:01:17 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.040 |  |
| 2026-04-23 12:01:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-04-23 12:01:11 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 12:00:37 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-04-23 12:00:12 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:00:09 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:56:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 12:29:43 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-23 12:01:11 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 12:03:16 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 12:03:45 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 12:05:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:01:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:06:10 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:06:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:07:29 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:01:50 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 12:04:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:05:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:04:49 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:03:17 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:05:48 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:02:08 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-04-23 12:12:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2026-04-23 12:03:08 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-04-23 12:07:49 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-04-23 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:00:09 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:02:09 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:02:59 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:00:12 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:03:13 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:04:14 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-23 12:02:19 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2026-04-23 12:03:07 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-23 12:00:37 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-04-23 12:03:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-04-23 12:01:17 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.040 |  |
| 2026-04-23 12:01:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-04-23 12:04:24 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.043 |  |
| 2026-04-23 12:02:41 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.054 |  |
| 2026-04-23 12:02:01 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.059 |  |
| 2026-04-23 12:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-23 12:03:10 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.060 |  |
| 2026-04-23 12:10:03 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.066 |  |
| 2026-04-23 12:02:06 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
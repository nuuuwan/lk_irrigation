# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_06:28:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,895 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 06:28:40 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-05-26 06:15:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:12:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-26 06:12:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.017 |  |
| 2026-05-26 06:09:42 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 06:08:27 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 06:06:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-26 06:06:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.092 |  |
| 2026-05-26 06:05:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:33 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 06:05:22 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:19 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-26 06:05:08 | Rathnapura (Kalu Ganga) | 5.01 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-26 06:04:34 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-26 06:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-26 06:04:10 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 06:04:02 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.014 |  |
| 2026-05-26 06:03:42 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:03:33 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.005 |  |
| 2026-05-26 06:03:31 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-26 06:03:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-05-26 06:03:04 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-26 06:03:02 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 06:02:52 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-26 06:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-05-26 06:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 06:02:21 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.122 |  |
| 2026-05-26 06:02:19 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:49 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 06:01:34 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:07 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.022 |  |
| 2026-05-26 06:00:55 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 06:00:45 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 06:00:34 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:00:15 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 06:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-26 06:03:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-05-26 06:04:34 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-26 06:03:04 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-26 06:05:08 | Rathnapura (Kalu Ganga) | 5.01 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-26 06:06:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-26 06:12:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-26 06:00:45 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 06:02:52 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-26 06:00:15 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-26 06:09:42 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 06:05:33 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 06:00:55 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 06:08:27 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 06:04:10 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 06:01:49 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 05:41:07 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-26 06:03:02 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 06:03:33 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.005 |  |
| 2026-05-26 06:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:00:34 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:03:42 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:15:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:22 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:01:34 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:02:19 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:19 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 06:03:31 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-26 06:04:02 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.014 |  |
| 2026-05-26 06:12:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.017 |  |
| 2026-05-26 06:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 06:01:07 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.022 |  |
| 2026-05-26 06:28:40 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-05-26 06:06:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.092 |  |
| 2026-05-26 06:02:21 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.122 |  |
| 2026-05-26 05:07:07 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
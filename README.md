# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_12:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 12:22:21 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.008 |  |
| 2026-04-16 12:15:19 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:08:04 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:06:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:54 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:05:46 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:28 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.068 |  |
| 2026-04-16 12:05:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:01 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.072 |  |
| 2026-04-16 12:04:52 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-16 12:04:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:03:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:03:45 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-04-16 12:03:33 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-16 12:03:31 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-16 12:03:26 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-04-16 12:03:20 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:03:17 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.057 |  |
| 2026-04-16 12:03:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:03:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.036 |  |
| 2026-04-16 12:03:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 12:03:05 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 12:02:33 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:17 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:12 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.120 |  |
| 2026-04-16 12:02:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-04-16 12:02:08 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:04 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:01:40 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-04-16 12:01:37 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -2.000 |  |
| 2026-04-16 12:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:01:19 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -2.000 |  |
| 2026-04-16 12:01:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:00:56 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-16 12:00:35 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:00:33 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.033 |  |
| 2026-04-16 12:00:16 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-16 12:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 12:00:56 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-16 12:03:31 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-16 12:00:16 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-16 12:03:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 12:03:05 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 12:02:04 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:17 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:01:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:03:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:00:35 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:15:19 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:08 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:46 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:05:54 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:02:33 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:04:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:06:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:08:04 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:22:21 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.008 |  |
| 2026-04-16 12:03:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:03:20 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:05:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-16 12:03:26 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-04-16 12:04:52 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-16 12:03:33 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-16 12:00:33 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.033 |  |
| 2026-04-16 12:03:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.036 |  |
| 2026-04-16 12:03:45 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-04-16 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-04-16 12:01:40 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-04-16 12:03:17 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.057 |  |
| 2026-04-16 12:05:28 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.068 |  |
| 2026-04-16 12:05:01 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.072 |  |
| 2026-04-16 12:02:12 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.120 |  |
| 2026-04-16 12:01:37 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
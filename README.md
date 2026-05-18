# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_10:25:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,096 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 10:25:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-05-18 10:14:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:13:24 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:10:12 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:09:03 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:08:25 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:08:22 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-05-18 10:07:39 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-18 10:07:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:06:33 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-05-18 10:06:22 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:05:51 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:05:30 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.042 |  |
| 2026-05-18 10:05:26 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.059 |  |
| 2026-05-18 10:05:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-18 10:05:07 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:04:48 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:04:12 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:03:31 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.069 |  |
| 2026-05-18 10:03:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:03:24 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.030 |  |
| 2026-05-18 10:03:19 | Thanthirimale (Malwathu Oya) | 3.15 | 🟢 Normal | -0.068 |  |
| 2026-05-18 10:03:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.030 |  |
| 2026-05-18 10:03:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | -0.070 |  |
| 2026-05-18 10:02:41 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:23 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-18 10:02:21 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:19 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.082 |  |
| 2026-05-18 10:02:06 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | -0.080 |  |
| 2026-05-18 10:02:05 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:04 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:51 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.234 |  |
| 2026-05-18 10:01:42 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 10:01:38 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-05-18 10:01:28 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:21 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:03 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | -0.070 |  |
| 2026-05-18 10:05:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-18 10:07:39 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-18 10:02:21 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:13:24 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:03:25 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:10:12 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:14:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:03:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:21 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:04:48 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:41 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:08:25 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:03:27 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:04:12 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:09:03 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:05:51 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:06:22 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:03 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:05:07 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:07:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:28 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:02:05 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 10:01:42 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 10:02:23 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-18 10:08:22 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-05-18 10:06:33 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-05-18 10:25:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-05-18 10:03:24 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.030 |  |
| 2026-05-18 10:03:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.030 |  |
| 2026-05-18 10:05:30 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.042 |  |
| 2026-05-18 10:01:38 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-05-18 10:05:26 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.059 |  |
| 2026-05-18 10:03:19 | Thanthirimale (Malwathu Oya) | 3.15 | 🟢 Normal | -0.068 |  |
| 2026-05-18 10:03:31 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.069 |  |
| 2026-05-18 10:02:06 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | -0.080 |  |
| 2026-05-18 10:02:19 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.082 |  |
| 2026-05-18 10:01:51 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
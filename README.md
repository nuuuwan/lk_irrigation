# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_06:29:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,674 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 06:29:17 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.001 |  |
| 2026-05-28 06:20:11 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:14:01 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 06:11:05 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:10:12 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-05-28 06:10:11 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-05-28 06:10:04 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-05-28 06:08:31 | Hanwella (Kelani Ganga) | 4.53 | 🟢 Normal | -0.009 |  |
| 2026-05-28 06:08:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-28 06:06:33 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:32 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:30 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:13 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:04:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:04:02 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:03:41 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-05-28 06:03:30 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.133 |  |
| 2026-05-28 06:03:27 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:03:22 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.102 |  |
| 2026-05-28 06:03:16 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:03:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-28 06:03:12 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-28 06:02:59 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:49 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.059 |  |
| 2026-05-28 06:02:44 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:43 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-05-28 06:02:42 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-05-28 06:02:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:14 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:01:58 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.090 |  |
| 2026-05-28 06:01:51 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-05-28 06:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 2.227 | 🔺 Rising |
| 2026-05-28 06:01:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.061 |  |
| 2026-05-28 06:01:00 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-28 06:00:43 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:00:23 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | -0.073 |  |
| 2026-05-28 05:58:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.78 | 🟡 Alert | 2.227 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 06:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 2.227 | 🔺 Rising |
| 2026-05-28 06:00:23 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | -0.073 |  |
| 2026-05-28 06:10:12 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-05-28 06:03:12 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-28 06:08:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 06:03:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-28 06:01:00 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-28 06:14:01 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 05:02:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:00:43 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:01:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:44 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:13 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:14 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:32 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:03:16 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:04:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:06:33 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:05:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:20:11 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:59 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:11:05 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:04:02 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:05:30 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 06:29:17 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.001 |  |
| 2026-05-28 06:10:04 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-05-28 06:08:31 | Hanwella (Kelani Ganga) | 4.53 | 🟢 Normal | -0.009 |  |
| 2026-05-28 06:02:43 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-05-28 06:03:41 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-05-28 06:01:51 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-05-28 06:02:42 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-05-28 06:02:49 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.059 |  |
| 2026-05-28 06:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.061 |  |
| 2026-05-28 06:01:58 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.090 |  |
| 2026-05-28 06:03:22 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.102 |  |
| 2026-05-28 06:03:30 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
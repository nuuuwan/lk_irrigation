# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_08:38:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 08:38:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:15:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.896 |  |
| 2026-05-08 08:11:41 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-08 08:11:18 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.057 |  |
| 2026-05-08 08:11:11 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 08:10:47 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-08 08:09:12 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:07:06 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-08 08:06:50 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-08 08:06:47 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 08:06:43 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.079 |  |
| 2026-05-08 08:06:23 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-05-08 08:06:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:06:10 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.028 |  |
| 2026-05-08 08:05:38 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.272 |  |
| 2026-05-08 08:05:18 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-08 08:04:44 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.115 |  |
| 2026-05-08 08:04:15 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.231 |  |
| 2026-05-08 08:04:02 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-08 08:03:51 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | -0.896 |  |
| 2026-05-08 08:03:41 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.061 |  |
| 2026-05-08 08:03:23 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.079 |  |
| 2026-05-08 08:02:58 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.081 |  |
| 2026-05-08 08:02:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-05-08 08:02:57 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:02:48 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-05-08 08:02:48 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2026-05-08 08:02:43 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:02:40 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.080 |  |
| 2026-05-08 08:02:06 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.272 |  |
| 2026-05-08 08:01:56 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:01:56 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-05-08 08:01:49 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.060 |  |
| 2026-05-08 08:01:36 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 08:01:07 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -1.004 |  |
| 2026-05-08 08:00:50 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.061 |  |
| 2026-05-08 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:00:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 08:04:02 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-08 08:10:47 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-08 08:05:18 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-08 08:07:06 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-08 08:11:11 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 08:00:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 08:02:43 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:01:49 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 08:06:47 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 08:11:41 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-08 08:38:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:02:57 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:01:56 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-08 08:09:12 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:06:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:03:51 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.009 |  |
| 2026-05-08 08:01:36 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 08:06:50 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-08 08:02:48 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-05-08 08:06:10 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.028 |  |
| 2026-05-08 08:02:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-05-08 08:06:23 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-05-08 08:01:56 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-05-08 08:11:18 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.057 |  |
| 2026-05-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.060 |  |
| 2026-05-08 08:00:50 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.061 |  |
| 2026-05-08 08:03:41 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.061 |  |
| 2026-05-08 08:06:43 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.079 |  |
| 2026-05-08 08:03:23 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.079 |  |
| 2026-05-08 08:02:40 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.080 |  |
| 2026-05-08 08:02:58 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.081 |  |
| 2026-05-08 08:04:44 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.115 |  |
| 2026-05-08 08:02:48 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2026-05-08 08:04:15 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.231 |  |
| 2026-05-08 08:02:06 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.272 |  |
| 2026-05-08 08:05:38 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.272 |  |
| 2026-05-08 08:15:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.896 |  |
| 2026-05-08 08:01:07 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -1.004 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
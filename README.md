# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_07:18:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 07:18:31 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:16:33 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 07:14:37 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.078 |  |
| 2026-04-28 07:13:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.017 |  |
| 2026-04-28 07:12:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:12:23 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 07:11:45 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 07:11:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:10:33 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:08:08 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:07:01 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-04-28 07:06:41 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:06:39 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-04-28 07:06:22 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.057 |  |
| 2026-04-28 07:05:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:05:44 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.218 |  |
| 2026-04-28 07:05:33 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 07:04:56 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 07:04:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-04-28 07:04:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-04-28 07:04:09 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.039 |  |
| 2026-04-28 07:04:06 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-28 07:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-28 07:03:17 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:03:08 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2026-04-28 07:03:08 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.159 |  |
| 2026-04-28 07:03:01 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.118 |  |
| 2026-04-28 07:02:58 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-28 07:02:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 07:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:02:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:02:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:01:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:01:45 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 07:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:00:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-28 07:00:18 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.080 |  |
| 2026-04-28 06:59:43 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:59:10 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:32:56 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 07:04:06 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-28 07:02:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-28 07:00:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-28 07:16:33 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 07:01:45 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 06:01:19 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-28 07:11:45 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 07:02:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 07:04:56 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 07:05:33 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 07:01:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:02:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:05:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:06:41 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:03:17 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:18:31 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:10:33 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:12:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:11:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:06:39 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-04-28 07:02:58 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-28 07:13:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.017 |  |
| 2026-04-28 07:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-28 07:07:01 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-04-28 07:12:23 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 07:03:08 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2026-04-28 07:04:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-04-28 06:02:53 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-04-28 07:04:09 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.039 |  |
| 2026-04-28 07:06:22 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.057 |  |
| 2026-04-28 07:04:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-04-28 07:14:37 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.078 |  |
| 2026-04-28 07:00:18 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.080 |  |
| 2026-04-28 07:03:01 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.118 |  |
| 2026-04-28 07:03:08 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.159 |  |
| 2026-04-28 07:05:44 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
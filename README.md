# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_07:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 07:20:37 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:19:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:17:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:14:22 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-01-16 07:13:49 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.008 |  |
| 2026-01-16 07:13:49 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:11:39 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:09:05 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:08:41 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-16 07:08:25 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-16 07:07:22 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:06:46 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.055 |  |
| 2026-01-16 07:05:17 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-01-16 07:05:16 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-01-16 07:04:50 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.031 |  |
| 2026-01-16 07:04:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:04 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.020 |  |
| 2026-01-16 07:04:03 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:02 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.039 |  |
| 2026-01-16 07:03:59 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.071 |  |
| 2026-01-16 07:03:53 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.006 |  |
| 2026-01-16 07:03:43 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-16 07:03:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.095 |  |
| 2026-01-16 07:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 07:02:55 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 07:02:49 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 07:02:28 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:02:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:02:12 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.030 |  |
| 2026-01-16 07:02:09 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 07:02:07 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:01:48 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:01:39 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-16 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:00:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 06:59:27 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-01-16 06:43:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 07:01:39 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-16 07:08:25 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-16 07:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 07:02:09 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 07:00:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:01:48 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:02:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:02:28 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:11:39 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:07:22 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:17:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:50 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:04:03 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:09:05 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:20:37 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:13:49 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:19:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:02:07 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:03:53 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.006 |  |
| 2026-01-16 07:13:49 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.008 |  |
| 2026-01-16 07:14:22 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-01-16 07:08:41 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-16 07:02:55 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 07:02:49 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-16 06:59:27 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-01-16 06:04:15 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.013 |  |
| 2026-01-16 06:06:06 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.015 |  |
| 2026-01-16 07:04:04 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.020 |  |
| 2026-01-16 07:03:43 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-01-16 07:02:12 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.030 |  |
| 2026-01-16 07:05:16 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-01-16 07:04:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.031 |  |
| 2026-01-16 07:04:02 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.039 |  |
| 2026-01-16 07:06:46 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.055 |  |
| 2026-01-16 07:05:17 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-01-16 07:03:59 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.071 |  |
| 2026-01-16 07:03:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
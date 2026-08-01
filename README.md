# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_19:23:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 19:23:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-01 19:21:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-08-01 19:12:48 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.067 |  |
| 2026-08-01 19:12:12 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.179 |  |
| 2026-08-01 19:11:37 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:08:44 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-08-01 19:07:39 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:07:33 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.052 |  |
| 2026-08-01 19:07:33 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:07:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:07:12 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2026-08-01 19:06:47 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.549 |  |
| 2026-08-01 19:06:38 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:06:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:05:05 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-08-01 19:04:48 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 19:04:30 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:04:28 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-08-01 19:03:18 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.199 |  |
| 2026-08-01 19:03:15 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-01 19:02:58 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:02:57 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:02:31 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.102 |  |
| 2026-08-01 19:02:23 | Hanwella (Kelani Ganga) | 5.44 | 🟢 Normal | -0.091 |  |
| 2026-08-01 19:02:21 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-01 19:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 19:01:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 19:01:14 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-08-01 19:01:09 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 19:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-01 19:00:51 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:38 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 19:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-01 19:03:15 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-01 19:04:48 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 19:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 19:01:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 19:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 19:23:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-01 19:07:39 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:02:57 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:38 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:07:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:04:02 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:06:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:51 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:11:37 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:04:30 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:07:33 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:01:09 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:02:58 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:21:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-08-01 19:04:28 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-08-01 19:05:05 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-08-01 19:02:21 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-01 19:07:12 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 19:07:33 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.052 |  |
| 2026-08-01 19:08:44 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-08-01 19:12:48 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.067 |  |
| 2026-08-01 19:01:14 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-08-01 19:02:23 | Hanwella (Kelani Ganga) | 5.44 | 🟢 Normal | -0.091 |  |
| 2026-08-01 19:02:31 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.102 |  |
| 2026-08-01 19:12:12 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.179 |  |
| 2026-08-01 19:03:18 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.199 |  |
| 2026-08-01 19:06:47 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.549 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_11:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 11:11:25 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.028 |  |
| 2026-06-13 11:10:27 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:09:58 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:08:53 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:08:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-06-13 11:07:28 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:07:10 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.069 |  |
| 2026-06-13 11:06:51 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:06:42 | Giriulla (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-06-13 11:06:34 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-13 11:06:25 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-06-13 11:06:21 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 11:05:57 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:05:12 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-06-13 11:05:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-13 11:04:52 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-06-13 11:04:42 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-13 11:04:38 | Rathnapura (Kalu Ganga) | 5.54 | 🟡 Alert | -0.090 |  |
| 2026-06-13 11:04:31 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:04:31 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:04:15 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.121 |  |
| 2026-06-13 11:04:06 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:03:46 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:03:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-06-13 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.45 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 11:02:15 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 11:02:09 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:02:07 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:01:51 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.052 |  |
| 2026-06-13 11:01:49 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-13 11:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:01:34 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:01:32 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-06-13 11:01:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:00:54 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-13 10:59:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.45 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 11:06:21 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 11:01:51 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.052 |  |
| 2026-06-13 11:04:38 | Rathnapura (Kalu Ganga) | 5.54 | 🟡 Alert | -0.090 |  |
| 2026-06-13 11:06:34 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-13 11:05:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-13 10:04:20 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-13 11:04:42 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-13 11:02:15 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 10:02:07 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-13 11:03:46 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:06:51 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:05:57 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 11:07:28 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:10:27 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 10:04:00 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:04:06 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:01:34 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:04:31 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-06-13 10:59:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:04:31 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:01:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:00:54 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:08:53 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 11:08:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-06-13 11:02:07 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:02:09 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-13 11:03:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-06-13 11:06:42 | Giriulla (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-06-13 11:11:25 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.028 |  |
| 2026-06-13 11:01:49 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-13 11:05:12 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-06-13 11:04:52 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-06-13 11:01:32 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-06-13 11:06:25 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-06-13 11:07:10 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.069 |  |
| 2026-06-13 11:04:15 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
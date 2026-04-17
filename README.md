# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_19:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 19:13:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-17 19:12:11 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.018 |  |
| 2026-04-17 19:11:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:09:38 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-17 19:09:17 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:09:09 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:09:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-17 19:08:52 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-04-17 19:07:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.054 |  |
| 2026-04-17 19:07:14 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:06:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-17 19:06:27 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-17 19:06:05 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-17 19:05:51 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.056 |  |
| 2026-04-17 19:05:08 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.039 |  |
| 2026-04-17 19:04:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.087 |  |
| 2026-04-17 19:04:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:04:15 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-04-17 19:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:03:36 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.039 |  |
| 2026-04-17 19:03:33 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:03:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:42 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:39 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:29 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-17 19:02:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.160 |  |
| 2026-04-17 19:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:13 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 19:02:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:11 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-04-17 19:02:01 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 19:01:37 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:00:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:00:45 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-04-17 19:00:37 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 19:06:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-17 19:02:11 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-04-17 19:13:33 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-17 19:09:38 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-17 19:01:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 19:02:13 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:00:37 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:42 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:04:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:37 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:00:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:07:14 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:01:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:08:21 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:11:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:03:33 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:09:17 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:03:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:39 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 19:08:52 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-04-17 19:09:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-17 19:04:15 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-04-17 19:02:29 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-17 19:00:45 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-04-17 19:12:11 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.018 |  |
| 2026-04-17 19:06:05 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-17 19:03:36 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.039 |  |
| 2026-04-17 19:05:08 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.039 |  |
| 2026-04-17 19:07:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.054 |  |
| 2026-04-17 19:05:51 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.056 |  |
| 2026-04-17 19:04:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.087 |  |
| 2026-04-17 19:02:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
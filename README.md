# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_23:15:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 23:15:04 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:15:03 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-02-13 23:09:19 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:07:58 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 23:06:37 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:06:06 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-13 23:05:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:05:43 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 23:05:41 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-13 23:05:31 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:05:15 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.048 |  |
| 2026-02-13 23:04:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:24 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:23 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -1.895 |  |
| 2026-02-13 23:04:12 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:04:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:06 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:04 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -1.895 |  |
| 2026-02-13 23:03:51 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:03:16 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 23:03:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:43 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:02:34 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:28 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-02-13 23:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:01:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-02-13 23:01:15 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:01:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 23:01:06 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-13 22:32:59 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 23:05:41 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-13 23:03:16 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 23:01:06 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-13 22:03:03 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-13 23:05:43 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 23:01:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 23:07:58 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 22:03:39 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:34 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:32:59 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:03:25 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:09:19 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:09:59 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:02:28 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-13 22:04:10 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:06:37 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:03:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:24 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:05:31 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:15:04 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:04:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 23:15:03 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-02-13 23:04:12 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:05:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:03:51 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-13 22:00:18 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:02:43 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:01:15 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-13 23:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-02-13 23:06:06 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-13 22:21:40 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.043 |  |
| 2026-02-13 23:04:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.048 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 23:01:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-02-13 23:04:23 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
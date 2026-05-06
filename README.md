# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_23:42:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 23:42:51 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-05-06 23:16:10 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:09:55 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:09:00 | Holombuwa (Kelani Ganga) | 2.05 | 🟢 Normal | 0.542 | 🔺 Rising |
| 2026-05-06 23:07:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:07:36 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-06 23:06:40 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:06:16 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:06:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-06 23:05:38 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 23:09:00 | Holombuwa (Kelani Ganga) | 2.05 | 🟢 Normal | 0.542 | 🔺 Rising |
| 2026-05-06 23:01:30 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-06 23:06:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-06 23:04:32 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-06 22:08:31 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-06 23:07:36 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-06 23:01:11 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-06 23:04:56 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-06 23:01:49 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-06 23:06:40 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:00:14 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:02:12 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:01:49 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 23:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 23:01:16 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:01:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:04:40 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:01:50 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:16:10 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:00:57 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:00:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:00:57 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:05:38 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:09:55 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:03:00 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:06:16 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:01:30 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:02:58 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 23:02:26 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-06 23:04:21 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-06 23:42:51 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-05-06 23:02:26 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-06 23:03:16 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.032 |  |
| 2026-05-06 23:02:43 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
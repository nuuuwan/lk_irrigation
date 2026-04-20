# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_23:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,570 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 23:13:31 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:12:09 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-04-20 23:09:46 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-20 23:08:31 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.046 |  |
| 2026-04-20 23:08:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 23:07:29 | Thanamalwila (Kirindi Oya) | 4.69 | 🟡 Alert | 0.742 | 🔺 Rising |
| 2026-04-20 23:07:26 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-04-20 23:06:40 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 23:06:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-20 23:05:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:05:01 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-20 23:05:00 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-20 23:04:07 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.039 |  |
| 2026-04-20 23:03:42 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 23:03:13 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-20 23:03:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-04-20 23:02:34 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-20 23:02:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 23:02:16 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 23:02:09 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:51 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-04-20 23:01:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 23:01:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:26 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 23:01:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 23:01:14 | Kuda Oya (Kirindi Oya) | 4.90 | 🟢 Normal | -0.100 |  |
| 2026-04-20 23:00:46 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.119 |  |
| 2026-04-20 22:25:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 23:07:29 | Thanamalwila (Kirindi Oya) | 4.69 | 🟡 Alert | 0.742 | 🔺 Rising |
| 2026-04-20 22:04:26 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-04-20 23:12:09 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-04-20 23:07:26 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-04-20 23:05:01 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-20 23:06:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 23:05:00 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-20 23:03:13 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-20 23:09:46 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-20 22:05:36 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-20 23:01:26 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 22:25:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-20 23:02:16 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 23:02:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 23:03:42 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 23:08:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 23:06:40 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 23:01:15 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 23:01:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 23:03:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:09 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:13:31 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:01:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:05:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 23:02:37 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-04-20 22:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-20 23:04:07 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.039 |  |
| 2026-04-20 23:08:31 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.046 |  |
| 2026-04-20 23:02:34 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-20 21:19:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-04-20 23:01:51 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-04-20 23:01:14 | Kuda Oya (Kirindi Oya) | 4.90 | 🟢 Normal | -0.100 |  |
| 2026-04-20 23:00:46 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.119 |  |
| 2026-04-20 22:07:16 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
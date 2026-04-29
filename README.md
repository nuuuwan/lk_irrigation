# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_23:20:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 23:20:45 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.004 |  |
| 2026-04-29 23:17:43 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.037 |  |
| 2026-04-29 23:10:30 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:09:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:09:31 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 23:07:42 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-04-29 23:07:36 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:07:00 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2026-04-29 23:06:55 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-04-29 23:06:43 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-29 23:05:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-29 23:05:33 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 23:05:23 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:05:13 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-29 23:04:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:04:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:03:17 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:02:55 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:02:05 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.023 |  |
| 2026-04-29 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-29 23:01:53 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-04-29 23:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:33 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -252.000 |  |
| 2026-04-29 23:01:32 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -252.000 |  |
| 2026-04-29 23:01:31 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:01:19 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:17 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:00 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:57:37 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 23:01:53 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-04-29 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-29 23:05:13 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-29 23:05:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 23:06:43 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-29 22:00:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 23:09:31 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 23:05:33 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 23:01:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:19 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:02:52 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:17 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:09:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:11:47 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:04:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:57:37 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:10:30 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:03:17 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:01:00 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:04:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:02:55 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-04-29 23:20:45 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.004 |  |
| 2026-04-29 23:06:55 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-04-29 23:07:36 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:05:23 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:04:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:01:31 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-04-29 23:07:42 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-04-29 23:02:05 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.023 |  |
| 2026-04-29 23:07:00 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2026-04-29 23:17:43 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.037 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 23:01:33 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_08:35:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 08:35:26 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | -0.022 |  |
| 2026-01-14 08:16:32 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:15:12 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-01-14 08:12:19 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.044 |  |
| 2026-01-14 08:11:29 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.012 |  |
| 2026-01-14 08:10:43 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:10:16 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:08:49 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-14 08:08:06 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:07:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:07:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:07:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-14 08:06:55 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.026 |  |
| 2026-01-14 08:06:44 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:06:33 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-01-14 08:06:20 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:05:13 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-14 08:04:24 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:04:20 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:04:17 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 08:04:04 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-01-14 08:04:00 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:03:47 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-01-14 08:03:41 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.021 |  |
| 2026-01-14 08:03:32 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.019 |  |
| 2026-01-14 08:03:22 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:02:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-14 08:02:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:02:17 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:02:11 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-01-14 08:01:40 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:30 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:01:20 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:20 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:00:43 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:00:42 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.104 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 08:08:49 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-14 08:05:13 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-14 08:02:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:20 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:16:32 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:04:20 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:03:22 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:07:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:08:06 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:04:24 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:10:43 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:07:32 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:06:44 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:10:16 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:40 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:01:20 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 08:15:12 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-01-14 08:07:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-14 08:02:17 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:02:11 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:00:43 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:04:00 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:01:30 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:06:20 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-14 08:02:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-14 08:03:47 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-01-14 08:11:29 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.012 |  |
| 2026-01-14 08:03:32 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.019 |  |
| 2026-01-14 08:04:04 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-01-14 08:03:41 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.021 |  |
| 2026-01-14 08:06:33 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-01-14 08:35:26 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | -0.022 |  |
| 2026-01-14 08:06:55 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.026 |  |
| 2026-01-14 08:04:17 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 08:12:19 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.044 |  |
| 2026-01-14 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-01-14 08:00:42 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
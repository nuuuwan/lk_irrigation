# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_01:17:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 01:17:09 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:10:48 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:08:31 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-22 01:08:09 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-22 01:06:58 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:06:46 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.063 |  |
| 2026-07-22 01:06:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:06:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-07-22 01:05:31 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:28 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:06 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:04:39 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:04:15 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:04:02 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 01:03:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:42 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-22 01:02:41 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:30 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:29 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:23 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.041 |  |
| 2026-07-22 01:02:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:07 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-22 01:01:34 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-07-22 01:01:16 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:12 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.213 |  |
| 2026-07-22 01:01:10 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-07-22 01:00:54 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-22 00:58:34 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-22 01:08:31 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-22 01:08:09 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-22 01:02:42 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-22 01:04:02 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-22 01:01:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-22 01:02:41 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:00:54 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:29 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:17:09 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:06:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:12 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:06:58 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:06:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:03:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:16 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:06 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:07 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-22 00:02:24 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:10:48 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:34 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:04:39 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-22 00:16:19 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:02:30 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:00 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-22 00:02:55 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:04:15 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:28 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:05:31 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-22 01:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-07-22 01:01:10 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-07-21 18:04:58 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-07-22 01:05:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-07-21 21:13:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.036 |  |
| 2026-07-22 01:02:23 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.041 |  |
| 2026-07-22 01:06:46 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.063 |  |
| 2026-07-22 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
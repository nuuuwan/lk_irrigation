# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_22:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,828 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 22:22:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 22:10:31 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 22:08:38 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-01-13 22:08:34 | Horowpothana (Yan Oya) | 3.82 | 🟢 Normal | -0.040 |  |
| 2026-01-13 22:07:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:07:09 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 22:06:40 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:06:24 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-13 22:05:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:05:38 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.058 |  |
| 2026-01-13 22:05:28 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:05:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:05:20 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-13 22:05:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:04:53 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:04:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:49 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:02:59 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-13 22:02:50 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 22:02:40 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:02:27 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:02:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 22:02:15 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:01:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-13 22:01:44 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-13 22:01:25 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:01:06 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 22:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:00:56 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 22:08:38 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-01-13 22:02:59 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-13 22:05:20 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-13 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-13 22:01:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-13 22:02:50 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 22:10:31 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 22:07:09 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 22:22:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 22:02:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 22:01:06 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 22:04:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:05:28 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:01:25 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:49 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:06:40 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:07:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:02:40 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:02:27 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:05:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:07:09 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:04:53 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:13:08 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:03:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 22:06:24 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-13 22:05:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:00:56 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:01:44 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:02:15 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-01-13 22:05:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-13 20:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 22:08:34 | Horowpothana (Yan Oya) | 3.82 | 🟢 Normal | -0.040 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-13 22:05:38 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
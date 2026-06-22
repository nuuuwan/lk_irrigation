# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_08:07:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 08:07:53 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-06-22 08:07:53 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:07:24 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-22 08:06:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 08:06:32 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-22 08:06:12 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-22 08:05:47 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:05:40 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 08:05:29 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:05:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-06-22 08:04:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 08:03:58 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 08:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-06-22 08:03:33 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:27 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-06-22 08:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:19 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 08:02:55 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-22 08:02:42 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:02:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-22 08:02:15 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:02:04 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:01:59 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-22 08:01:57 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:01:30 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-06-22 08:01:16 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:00:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.030 |  |
| 2026-06-22 08:00:23 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:00:10 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.079 |  |
| 2026-06-22 07:38:05 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-06-22 07:33:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.003 |  |
| 2026-06-22 07:20:41 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.026 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 08:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-06-22 08:05:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-06-22 08:07:53 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-06-22 08:02:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-22 07:14:48 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-22 08:03:19 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 08:07:24 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-22 07:05:53 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 08:06:12 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-22 08:06:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 08:06:32 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-22 08:05:40 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 08:02:55 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-22 08:04:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 08:03:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 07:33:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.003 |  |
| 2026-06-22 08:01:16 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:02:04 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:33 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:01:57 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:05:47 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:14 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:00:23 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:07:53 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:02:42 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:03:57 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:03:58 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:05:29 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 08:02:15 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:10:52 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-22 08:01:59 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:03:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:01:51 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-22 08:01:30 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-06-22 08:00:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.030 |  |
| 2026-06-22 08:03:27 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-06-22 08:00:10 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
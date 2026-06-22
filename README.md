# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_03:30:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,819 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 03:30:37 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-23 03:30:35 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-23 03:30:34 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-23 03:29:38 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.016 |  |
| 2026-06-23 03:21:34 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-23 03:14:04 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.381 |  |
| 2026-06-23 03:11:26 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-23 03:11:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:10:27 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.027 |  |
| 2026-06-23 03:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.73 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-06-23 03:08:24 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 03:07:54 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.110 |  |
| 2026-06-23 03:07:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:06:45 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-23 03:06:35 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-23 03:06:32 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:06:31 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:06:08 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.224 |  |
| 2026-06-23 03:06:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-23 03:06:02 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-06-23 03:05:17 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:04:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-23 03:03:46 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-06-23 03:03:28 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-23 03:03:17 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:02:33 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:02:30 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:02:15 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-06-23 03:02:14 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:34 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 03:01:04 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-23 03:01:03 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 2.880 | 🔺 Rising |
| 2026-06-23 03:01:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:00:55 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 03:00:38 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | 2.880 | 🔺 Rising |
| 2026-06-23 02:50:32 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 03:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.73 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-06-23 03:03:46 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-06-23 03:30:37 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-23 03:01:03 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 2.880 | 🔺 Rising |
| 2026-06-23 03:02:15 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-06-23 03:06:35 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-23 03:03:28 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-23 03:21:34 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-23 03:11:26 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-23 03:06:45 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-23 02:43:27 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 03:06:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-23 03:08:24 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 03:01:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 01:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 03:00:55 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 03:01:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:02:09 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:06:32 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:11:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:34 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:02:14 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:02:33 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:05:17 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:07:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:03:17 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:04:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-23 03:01:04 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-23 03:06:02 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-06-23 03:29:38 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.016 |  |
| 2026-06-23 03:10:27 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.027 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 03:07:54 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.110 |  |
| 2026-06-23 03:06:08 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.224 |  |
| 2026-06-23 03:14:04 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
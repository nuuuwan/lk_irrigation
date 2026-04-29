# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_08:29:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,026 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 08:29:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:16:22 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:10:21 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:09:17 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-29 08:08:44 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-04-29 08:08:38 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:08:38 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:06:37 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:06:13 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:05:52 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.052 |  |
| 2026-04-29 08:05:49 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:05:40 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:05:37 | Thanthirimale (Malwathu Oya) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-04-29 08:05:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-04-29 08:05:23 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.019 |  |
| 2026-04-29 08:04:24 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.068 |  |
| 2026-04-29 08:04:07 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-04-29 08:04:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:03:52 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 08:03:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:03:37 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-29 08:03:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-29 08:03:28 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-29 08:03:13 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.094 |  |
| 2026-04-29 08:02:58 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:02:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:02:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.079 |  |
| 2026-04-29 08:02:33 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:02:28 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.020 |  |
| 2026-04-29 08:02:14 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:02:11 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-29 08:01:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:37 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-04-29 08:01:32 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-29 08:01:30 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:23 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:00:57 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.042 |  |
| 2026-04-29 07:39:51 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 08:02:11 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-29 08:03:28 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-29 08:03:37 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-29 08:03:52 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 07:16:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:29:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 07:16:23 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:10:21 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:06:37 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:04:24 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:03:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:02:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:04:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:02:58 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:05:49 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:08:38 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:06:13 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:01:30 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 08:08:38 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:02:33 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:05:40 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:02:14 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-29 08:08:44 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-04-29 08:05:37 | Thanthirimale (Malwathu Oya) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-04-29 08:05:23 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.019 |  |
| 2026-04-29 08:02:28 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.020 |  |
| 2026-04-29 08:01:32 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-29 08:04:07 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-04-29 08:09:17 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-29 08:03:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-29 08:05:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-04-29 08:01:37 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-04-29 08:00:57 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.042 |  |
| 2026-04-29 08:05:52 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.052 |  |
| 2026-04-29 08:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.068 |  |
| 2026-04-29 08:02:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.079 |  |
| 2026-04-29 08:03:13 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
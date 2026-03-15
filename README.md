# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_06:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 06:15:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:09:35 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:08:37 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 06:08:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-15 06:07:45 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 06:07:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:07:34 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 06:06:59 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:06:30 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:06:30 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-15 06:06:04 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.164 |  |
| 2026-03-15 06:06:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:05:58 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:05:37 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.041 |  |
| 2026-03-15 06:04:34 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 06:04:18 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.064 |  |
| 2026-03-15 06:04:08 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:04:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 06:03:54 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-15 06:03:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:03:40 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.070 |  |
| 2026-03-15 06:03:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-15 06:03:13 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.023 |  |
| 2026-03-15 06:03:11 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-03-15 06:02:46 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-15 06:02:18 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-15 06:01:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:34 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:31 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-15 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 06:01:11 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:07 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-15 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.160 |  |
| 2026-03-15 06:00:54 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.041 |  |
| 2026-03-15 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 06:00:39 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 05:57:05 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:55:49 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:46:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.160 |  |
| 2026-03-15 05:37:09 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-03-15 05:36:22 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-03-15 05:36:21 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 06:02:18 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-15 06:03:54 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-15 06:07:45 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 06:01:07 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-15 06:06:30 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-15 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 06:07:34 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 06:04:34 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 06:03:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-15 06:00:39 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 06:08:37 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 06:04:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 06:06:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:09:35 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:34 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:15:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:06:30 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:03:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:07:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:11 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:04:08 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:01:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:05:58 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:01:31 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:03:11 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:08:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-15 06:02:46 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-15 06:03:13 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.023 |  |
| 2026-03-15 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-15 06:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-03-15 06:05:37 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.041 |  |
| 2026-03-15 06:00:54 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.041 |  |
| 2026-03-15 06:04:18 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.064 |  |
| 2026-03-15 06:03:40 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.070 |  |
| 2026-03-15 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.160 |  |
| 2026-03-15 06:06:04 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
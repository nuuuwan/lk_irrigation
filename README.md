# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_03:07:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 03:07:09 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:05:36 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 03:05:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 03:05:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-06-07 03:04:54 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:04:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 03:04:50 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-06-07 03:04:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:04:19 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-06-07 03:03:42 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-07 03:03:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:10 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -1.565 |  |
| 2026-06-07 03:03:07 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 03:03:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:02:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 03:02:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-07 03:02:47 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -1.565 |  |
| 2026-06-07 03:01:39 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 02:37:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-07 02:30:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 03:02:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-07 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-07 03:03:07 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 03:05:36 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 02:06:35 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 03:02:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 03:04:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 02:04:15 | Rathnapura (Kalu Ganga) | 2.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 03:05:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 03:06:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:04:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 02:37:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:07:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 02:03:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-07 02:02:16 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:39 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 02:10:09 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:07:09 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:04:50 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-06-07 01:14:04 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.008 |  |
| 2026-06-07 03:04:54 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:42 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-07 02:01:35 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-06-07 01:08:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-06-07 03:04:19 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-06-07 00:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.023 |  |
| 2026-06-07 02:03:00 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-06-07 03:05:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-06-07 02:08:41 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.956 |  |
| 2026-06-07 03:03:10 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
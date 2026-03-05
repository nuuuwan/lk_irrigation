# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_09:14:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 09:14:43 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:10:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:09:12 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.037 |  |
| 2026-03-05 09:08:45 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:08:38 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-05 09:08:38 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:07:18 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 09:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:05:54 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-03-05 09:05:21 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-03-05 09:05:07 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:04:47 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:04:28 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:04:18 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:04:09 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-03-05 09:04:07 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-05 09:03:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-05 09:03:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-03-05 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-03-05 09:03:37 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 09:03:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:03:23 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:47 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 09:02:47 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.129 |  |
| 2026-03-05 09:02:45 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:32 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:10 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:02:04 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:50 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:50 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:47 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:01:35 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:00:37 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:00:23 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 09:03:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-05 09:02:47 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 09:07:18 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 09:03:37 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 09:04:07 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-05 09:00:23 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:04 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:03:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:50 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:09:12 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:45 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:05:07 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:08:38 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:14:43 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:08:45 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:04:18 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:00:37 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:02:32 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:35 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:04:47 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:01:50 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:03:23 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:10:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 09:05:21 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-03-05 09:01:47 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:04:28 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:02:10 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-05 09:08:38 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-05 09:04:09 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-03-05 09:03:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-03-05 09:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.037 |  |
| 2026-03-05 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-03-05 09:05:54 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-03-05 09:02:47 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
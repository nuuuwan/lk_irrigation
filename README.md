# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--30_15:04:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,825 measurements** from **38** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-27 20:03:23 | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood |
| 2025-11-27 13:00:40 | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood |
| 2025-11-28 15:00:24 | Thanthirimale (Malwathu Oya) | 10.30 | 🔴 Major Flood |
| 2025-11-28 06:04:09 | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood |
| 2025-11-30 15:02:43 | Nagalagam Street (Kelani Ganga) | 2.29 | 🔴 Major Flood |
| 2025-11-30 15:03:32 | Hanwella (Kelani Ganga) | 10.64 | 🔴 Major Flood |
| 2025-11-30 03:16:47 | Badalgama (Maha Oya) | 11.35 | 🔴 Major Flood |
| 2025-11-28 02:13:33 | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood |
| 2025-11-27 08:02:16 | Thaldena (Badulu Oya) | 4.25 | 🟠 Minor Flood |
| 2025-11-27 18:42:59 | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood |
| 2025-11-30 15:00:27 | Horowpothana (Yan Oya) | 7.55 | 🟠 Minor Flood |
| 2025-11-30 15:03:15 | Putupaula (Kalu Ganga) | 4.26 | 🟠 Minor Flood |
| 2025-11-30 15:02:26 | Dunamale (Aththanagalu Oya) | 5.04 | 🟠 Minor Flood |
| 2025-11-30 15:01:35 | Glencourse (Kelani Ganga) | 16.90 | 🟠 Minor Flood |
| 2025-11-30 14:07:45 | Rathnapura (Kalu Ganga) | 6.80 | 🟡 Alert |
| 2025-11-30 15:03:18 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal |
| 2025-11-30 15:00:44 | Nakkala (Kumbukkan Oya) | 1.83 | 🟢 Normal |
| 2025-11-30 15:03:26 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 15:03:47 | Norwood (Kehelgamu Oya) | 1.42 | 🟢 Normal |
| 2025-11-30 15:04:58 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal |
| 2025-11-30 14:02:43 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 15:03:14 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal |
| 2025-11-30 15:03:52 | Kuda Oya (Kuda Oya) | 2.03 | 🟢 Normal |
| 2025-11-30 15:04:16 | Urawa (Urubokka Ganga) | 0.84 | 🟢 Normal |
| 2025-11-30 14:04:52 | Deraniyagala (Seethawaka Ganga) | 1.64 | 🟢 Normal |
| 2025-11-30 15:01:16 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal |
| 2025-11-30 15:02:41 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal |
| 2025-11-30 15:03:23 | Katharagama (Menik Ganga) | 0.96 | 🟢 Normal |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal |
| 2025-11-30 15:02:58 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal |
| 2025-11-30 15:02:55 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal |
| 2025-11-30 15:04:21 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 15:00:51 | Yaka Wewa (Mukunu Oya) | 1.53 | 🟢 Normal |
| 2025-11-30 14:12:20 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal |
| 2025-11-30 15:02:17 | Magura (Maguru Ganga) | 3.22 | 🟢 Normal |
| 2025-11-30 14:10:24 | Giriulla (Maha Oya) | 4.25 | 🟢 Normal |
| 2025-11-30 15:04:00 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
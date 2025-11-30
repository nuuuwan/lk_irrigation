# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--30_17:26:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,892 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 17:26:28 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 17:10:39 | Giriulla (Maha Oya) | 4.05 | 🟢 Normal |
| 2025-11-30 17:09:11 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal |
| 2025-11-30 17:08:00 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 17:07:55 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal |
| 2025-11-30 17:06:26 | Hanwella (Kelani Ganga) | 10.55 | 🔴 Major Flood |
| 2025-11-30 17:06:01 | Magura (Kalu Ganga) | 2.99 | 🟢 Normal |
| 2025-11-30 17:05:49 | Nagalagam Street (Kelani Ganga) | 2.30 | 🔴 Major Flood |
| 2025-11-30 17:05:41 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert |
| 2025-11-30 17:05:33 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal |
| 2025-11-30 17:05:00 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal |
| 2025-11-30 17:04:51 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal |
| 2025-11-30 17:04:28 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal |
| 2025-11-30 17:04:11 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal |
| 2025-11-30 17:04:01 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal |
| 2025-11-30 17:03:54 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal |
| 2025-11-30 17:03:51 | Dunamale (Aththanagalu Oya) | 5.00 | 🟠 Minor Flood |
| 2025-11-30 17:03:41 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal |
| 2025-11-30 17:03:27 | Putupaula (Kalu Ganga) | 4.27 | 🟠 Minor Flood |
| 2025-11-30 17:03:12 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal |
| 2025-11-30 17:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.80 | 🟠 Minor Flood |
| 2025-11-30 17:02:52 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal |
| 2025-11-30 17:02:36 | Horowpothana (Yan Oya) | 7.53 | 🟠 Minor Flood |
| 2025-11-30 17:02:36 | Thanthirimale (Malwathu Oya) | 10.90 | 🔴 Major Flood |
| 2025-11-30 17:02:11 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal |
| 2025-11-30 17:02:10 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal |
| 2025-11-30 17:01:50 | Kuda Oya (Kirindi Oya) | 2.01 | 🟢 Normal |
| 2025-11-30 17:01:43 | Glencourse (Kelani Ganga) | 16.48 | 🟡 Alert |
| 2025-11-30 17:01:41 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal |
| 2025-11-30 17:01:08 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal |

## Latest by Station

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-27 20:03:23 | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood |
| 2025-11-27 13:00:40 | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood |
| 2025-11-28 06:04:09 | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood |
| 2025-11-30 17:05:49 | Nagalagam Street (Kelani Ganga) | 2.30 | 🔴 Major Flood |
| 2025-11-30 17:02:36 | Thanthirimale (Malwathu Oya) | 10.90 | 🔴 Major Flood |
| 2025-11-30 17:06:26 | Hanwella (Kelani Ganga) | 10.55 | 🔴 Major Flood |
| 2025-11-30 03:16:47 | Badalgama (Maha Oya) | 11.35 | 🔴 Major Flood |
| 2025-11-28 02:13:33 | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood |
| 2025-11-27 08:02:16 | Thaldena (Badulu Oya) | 4.25 | 🟠 Minor Flood |
| 2025-11-27 18:42:59 | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood |
| 2025-11-30 17:03:27 | Putupaula (Kalu Ganga) | 4.27 | 🟠 Minor Flood |
| 2025-11-30 17:02:36 | Horowpothana (Yan Oya) | 7.53 | 🟠 Minor Flood |
| 2025-11-30 17:03:51 | Dunamale (Aththanagalu Oya) | 5.00 | 🟠 Minor Flood |
| 2025-11-30 17:02:55 | Kalawellawa (Millakanda) (Kuda Ganga) | 7.80 | 🟠 Minor Flood |
| 2025-11-30 17:05:41 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert |
| 2025-11-30 17:01:43 | Glencourse (Kelani Ganga) | 16.48 | 🟡 Alert |
| 2025-11-30 17:02:11 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal |
| 2025-11-30 16:03:02 | Kithulgala (Kelani Ganga) | 2.66 | 🟢 Normal |
| 2025-11-30 17:04:01 | Norwood (Kehelgamu Oya) | 1.40 | 🟢 Normal |
| 2025-11-30 17:02:52 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal |
| 2025-11-30 17:05:00 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal |
| 2025-11-30 17:09:11 | Holombuwa (Gurugoda Oya) | 1.67 | 🟢 Normal |
| 2025-11-30 17:04:51 | Urawa (Urubokka Ganga) | 0.84 | 🟢 Normal |
| 2025-11-30 17:26:28 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 17:05:33 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal |
| 2025-11-30 17:04:28 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal |
| 2025-11-30 17:02:10 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal |
| 2025-11-30 17:01:50 | Kuda Oya (Kuda Oya) | 2.01 | 🟢 Normal |
| 2025-11-30 17:07:55 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal |
| 2025-11-30 17:04:11 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal |
| 2025-11-30 17:03:54 | Yaka Wewa (Mukunu Oya) | 1.48 | 🟢 Normal |
| 2025-11-30 17:03:41 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal |
| 2025-11-30 17:01:08 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal |
| 2025-11-30 17:01:41 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal |
| 2025-11-30 17:03:12 | Deraniyagala (Seethawaka Ganga) | 1.50 | 🟢 Normal |
| 2025-11-30 17:10:39 | Giriulla (Maha Oya) | 4.05 | 🟢 Normal |
| 2025-11-30 17:06:01 | Magura (Maguru Ganga) | 2.99 | 🟢 Normal |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
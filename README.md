# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_15:07:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,926 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 15:07:50 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:38 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:26 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:05:23 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:05:21 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-31 15:05:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2025-12-31 15:04:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:06 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:00 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:00 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:58 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-31 15:03:44 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-31 15:03:39 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:38 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:33 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:02:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-31 15:02:51 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-31 15:02:49 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 15:02:45 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.085 |  |
| 2025-12-31 15:02:35 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:02:17 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:02:00 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2025-12-31 15:01:49 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.221 |  |
| 2025-12-31 15:01:48 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:01:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:00:57 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:00:47 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.054 |  |
| 2025-12-31 15:00:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:00:15 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:59:26 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:50:19 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:37:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:14:58 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:12:58 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 15:02:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-31 15:02:51 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-31 15:05:21 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-31 15:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 15:01:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:00:15 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:00:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:02:17 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:05:23 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:38 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:00 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:06 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:26 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:59:26 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:39 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:00 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:07:50 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:33 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:06:38 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:02:35 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:03:58 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-31 15:02:49 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:00:57 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:01:48 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:03:44 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-31 14:01:15 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.031 |  |
| 2025-12-31 15:05:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2025-12-31 15:02:00 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2025-12-31 15:00:47 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.054 |  |
| 2025-12-31 15:02:45 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.085 |  |
| 2025-12-31 15:01:49 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
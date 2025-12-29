# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_21:17:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 21:17:52 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2025-12-29 21:17:05 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:14:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:12:39 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2025-12-29 21:10:06 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:09:05 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:08:38 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:07:46 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:07:40 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.040 |  |
| 2025-12-29 21:07:39 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-29 21:07:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 21:06:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2025-12-29 21:06:12 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:05:25 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:05:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:05:07 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 21:04:28 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 21:04:25 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:04:20 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 21:04:12 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2025-12-29 21:03:48 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:03:48 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:03:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 21:03:06 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:48 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2025-12-29 21:02:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:33 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:33 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:18 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-29 21:01:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-29 21:01:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.026 |  |
| 2025-12-29 21:01:23 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-29 21:01:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-29 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 21:04:12 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2025-12-29 21:01:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-29 21:04:20 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 21:05:07 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 21:04:28 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 21:01:23 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-29 20:02:00 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 21:03:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 21:07:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 21:04:25 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:03:48 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:05:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:05:25 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:10:06 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:14:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:33 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:48 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:06:12 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:03:06 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:08:38 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:03:48 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:33 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:17:05 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:07:46 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:17:52 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2025-12-29 21:07:39 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 21:02:18 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-29 21:12:39 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2025-12-29 21:01:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-29 21:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.026 |  |
| 2025-12-29 21:06:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2025-12-29 21:07:40 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.040 |  |
| 2025-12-29 21:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
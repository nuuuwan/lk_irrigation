# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_12:10:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 12:10:29 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2025-12-29 12:08:59 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.005 |  |
| 2025-12-29 12:08:01 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 12:07:59 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.036 |  |
| 2025-12-29 12:07:03 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2025-12-29 12:06:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 12:05:06 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 12:05:06 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 12:05:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2025-12-29 12:04:47 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:04:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:03:29 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:03:06 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 12:02:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:48 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-29 12:02:47 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.074 |  |
| 2025-12-29 12:02:38 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.072 |  |
| 2025-12-29 12:02:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:30 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 12:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:27 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:03 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:01:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:01:01 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-29 12:00:52 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 12:00:51 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:42 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:34 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:29 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:34:32 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.036 |  |
| 2025-12-29 11:17:27 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2025-12-29 11:16:41 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-29 11:16:26 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 12:01:01 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-29 12:02:48 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-29 12:02:30 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 12:05:06 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 11:05:57 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 12:06:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 11:02:14 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 12:00:52 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 12:05:06 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 12:08:01 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 12:00:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:34 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:03 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:04:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:01:57 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:27 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:03:29 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:29 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:42 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:04:47 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:00:51 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 12:08:59 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.005 |  |
| 2025-12-29 11:17:27 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2025-12-29 11:05:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:08:44 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-29 12:03:06 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 12:10:29 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2025-12-29 12:07:03 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2025-12-29 12:07:59 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.036 |  |
| 2025-12-29 12:05:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2025-12-29 12:02:38 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.072 |  |
| 2025-12-29 12:02:47 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
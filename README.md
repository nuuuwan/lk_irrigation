# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_12:10:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 12:10:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:39 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:08:59 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.045 |  |
| 2025-12-14 12:08:11 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.036 |  |
| 2025-12-14 12:07:51 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:42 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:06:53 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:06:01 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:05:52 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:05:13 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:04:42 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:04:22 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:04:14 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.032 |  |
| 2025-12-14 12:04:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2025-12-14 12:04:01 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:04:00 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2025-12-14 12:03:45 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:03:39 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 12:03:27 | Weraganthota (Mahaweli Ganga) | -1.01 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-14 12:03:12 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:03:09 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:02:59 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:02:58 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:35 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.083 |  |
| 2025-12-14 12:02:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:23 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.021 |  |
| 2025-12-14 12:02:22 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 12:02:21 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:12 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:01:47 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:01:37 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:01:35 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.061 |  |
| 2025-12-14 12:01:21 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.022 |  |
| 2025-12-14 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:00:15 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:00:07 | Horowpothana (Yan Oya) | 4.48 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 12:03:27 | Weraganthota (Mahaweli Ganga) | -1.01 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-14 12:02:22 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 12:03:39 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 12:07:42 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:51 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:03:09 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:06:01 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:39 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:02:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:03:12 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:04:22 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:05:52 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:10:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:08:15 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:04:01 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:01:47 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:01:37 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:21 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:00:15 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:58 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:23 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:12 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:05:13 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:03:45 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:04:42 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2025-12-14 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.021 |  |
| 2025-12-14 12:01:21 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.022 |  |
| 2025-12-14 12:04:00 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2025-12-14 12:04:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2025-12-14 12:04:14 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.032 |  |
| 2025-12-14 12:08:11 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.036 |  |
| 2025-12-14 12:08:59 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.045 |  |
| 2025-12-14 12:00:07 | Horowpothana (Yan Oya) | 4.48 | 🟢 Normal | -0.050 |  |
| 2025-12-14 12:01:35 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.061 |  |
| 2025-12-14 12:02:35 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
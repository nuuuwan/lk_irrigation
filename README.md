# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_10:45:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,841 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 10:45:14 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:36:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:20:02 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:18:32 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:17:49 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:10:51 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:10:49 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:08:27 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:07:08 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:06:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:06:02 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-30 10:05:22 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-30 10:05:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-30 10:04:55 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:04:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:53 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:37 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:17 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.051 |  |
| 2025-12-30 10:03:03 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.011 |  |
| 2025-12-30 10:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-30 10:03:00 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-30 10:02:59 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:34 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.214 |  |
| 2025-12-30 10:02:33 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-30 10:02:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:11 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.050 |  |
| 2025-12-30 10:01:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:38 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 10:01:19 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.014 |  |
| 2025-12-30 10:01:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:02 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:02 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.017 |  |
| 2025-12-30 10:00:23 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 10:05:22 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-30 10:01:38 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 10:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-30 10:01:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:06:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:36:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:10:51 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:04:55 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:17 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:33 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:04:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:08:27 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:53 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:11 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:06:02 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:03:37 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:45:14 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:01:02 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:10:49 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:18:32 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:20:02 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:02:59 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:17:49 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-30 10:03:00 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-30 10:00:23 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2025-12-30 10:03:03 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.011 |  |
| 2025-12-30 09:07:10 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2025-12-30 10:01:19 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.014 |  |
| 2025-12-30 10:01:02 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.017 |  |
| 2025-12-30 10:02:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-30 10:05:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-30 10:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.050 |  |
| 2025-12-30 10:03:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.051 |  |
| 2025-12-30 10:02:34 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_17:01:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 17:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:01:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-16 17:01:34 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:01:08 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:00:25 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:21:12 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-16 16:18:02 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:12:22 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 16:03:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-06-16 16:00:50 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-16 16:04:41 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-16 16:21:12 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-16 16:02:15 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 16:01:27 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 17:01:08 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:10:28 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:06:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:01:05 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:01:34 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:03:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:07:46 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-16 17:00:25 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:08:05 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:02:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:02:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:06:54 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:02:58 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:02:28 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 16:10:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.009 |  |
| 2026-06-16 16:04:36 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-06-16 16:03:25 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:02:22 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 17:01:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:04:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:00:53 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:00:36 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:02:31 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:12:22 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-16 16:06:12 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.012 |  |
| 2026-06-16 16:09:51 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-06-16 16:04:19 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-06-16 16:07:44 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-06-16 16:02:41 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-16 16:03:45 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.040 |  |
| 2026-06-16 16:10:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
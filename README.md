# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_11:16:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 11:16:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:14:14 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-06-18 11:11:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.046 |  |
| 2026-06-18 11:11:17 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.071 |  |
| 2026-06-18 11:09:11 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.040 |  |
| 2026-06-18 11:08:29 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-18 11:08:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 11:08:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-06-18 11:07:46 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 11:07:21 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-06-18 11:05:22 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 11:04:48 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.049 |  |
| 2026-06-18 11:04:01 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-06-18 11:03:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:03:38 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-18 11:03:28 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.073 |  |
| 2026-06-18 11:03:01 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 11:02:51 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:40 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 11:02:36 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-18 11:02:34 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 11:02:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-18 11:02:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:02:03 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-06-18 11:01:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:01:20 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:00:54 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:00:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.012 |  |
| 2026-06-18 11:00:28 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:00:08 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 10:59:19 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 11:02:36 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-18 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-18 10:06:55 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-18 11:08:29 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-18 11:03:38 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-18 11:03:01 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 11:07:46 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 11:02:34 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 11:05:22 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 11:02:40 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 11:08:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 11:00:08 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:03:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 10:03:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:02:51 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:16:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:01:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:01:20 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 11:14:14 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-06-18 11:07:21 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-06-18 11:00:54 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:02:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:00:28 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 11:00:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.012 |  |
| 2026-06-18 11:08:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-06-18 10:26:36 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.023 |  |
| 2026-06-18 11:09:11 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.040 |  |
| 2026-06-18 11:11:55 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.046 |  |
| 2026-06-18 11:04:48 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.049 |  |
| 2026-06-18 10:08:26 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.050 |  |
| 2026-06-18 11:04:01 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-06-18 11:02:03 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-06-18 11:11:17 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.071 |  |
| 2026-06-18 11:03:28 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
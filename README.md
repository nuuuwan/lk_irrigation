# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_04:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 04:17:01 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-04-26 04:16:22 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.008 |  |
| 2026-04-26 04:08:41 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:07:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:07:22 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:06:15 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:06:00 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:05:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:05:22 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:04:51 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-26 04:04:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:04:15 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.014 |  |
| 2026-04-26 04:04:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:03:49 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 04:03:34 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:03:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:52 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-26 04:02:36 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:02:13 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:01:55 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-04-26 04:01:54 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:01:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.080 |  |
| 2026-04-26 04:01:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:01:37 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 04:01:13 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 04:01:09 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:00:31 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 03:26:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-26 04:04:51 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-26 00:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-26 04:03:49 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 04:01:13 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 04:01:37 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 04:07:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:01:09 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:13 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:04:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:01:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:05:22 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:03:34 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:06:15 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:03:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:02:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 03:09:02 | Katharagama (Menik Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:04:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:06:00 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:05:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:17:01 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-04-26 04:16:22 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.008 |  |
| 2026-04-26 04:08:41 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-26 03:02:26 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:01:54 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:00:31 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:02:36 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:07:22 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:02:52 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-26 04:01:55 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-04-26 04:04:15 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.014 |  |
| 2026-04-26 02:59:30 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.017 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-26 04:01:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
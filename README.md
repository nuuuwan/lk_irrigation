# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_17:02:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 17:02:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-03 17:02:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 17:01:44 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:01:38 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:26 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-01-03 17:01:12 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:11 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:51 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 17:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:05 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:53:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.012 |  |
| 2026-01-03 16:36:41 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:08:47 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:07:43 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:07:32 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:07:27 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 16:07:02 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-03 16:06:19 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.022 |  |
| 2026-01-03 16:06:08 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:05:27 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 16:03:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-03 17:02:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 16:02:57 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 16:02:38 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 17:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:02:13 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:07:43 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:00:21 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:01:44 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:02:21 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:07:32 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:06:08 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:36:41 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:56:51 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:05:27 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-01-03 16:07:02 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-03 17:02:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:38 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:51 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-03 16:03:08 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-03 16:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:11 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:12 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 16:04:29 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-03 16:03:42 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-01-03 16:03:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-01-03 16:53:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.012 |  |
| 2026-01-03 15:02:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.014 |  |
| 2026-01-03 17:00:05 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:08:47 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:03:10 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-01-03 17:01:26 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-01-03 16:01:38 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 16:04:05 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.059 |  |
| 2026-01-03 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-03 16:03:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_06:02:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 06:02:39 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 06:02:36 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 06:02:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:02:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-08 06:02:22 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:08 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:04 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 06:01:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:01:15 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-08 06:01:06 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.798 |  |
| 2026-04-08 06:00:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -1.895 |  |
| 2026-04-08 06:00:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 06:00:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:00:29 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -1.895 |  |
| 2026-04-08 05:56:34 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.006 |  |
| 2026-04-08 05:46:43 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:19:28 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.008 |  |
| 2026-04-08 05:14:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-08 05:13:45 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-08 05:13:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-08 05:10:59 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-08 05:10:40 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-08 05:10:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.082 |  |
| 2026-04-08 05:09:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 05:14:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-08 03:22:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-08 06:02:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-08 06:02:36 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 06:00:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 06:01:15 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-08 06:02:39 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 05:04:19 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 05:13:45 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-08 06:02:04 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 05:03:05 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:00:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:04:07 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:03:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:22 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:08 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:04:25 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:07:25 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:14:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:06:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:01:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:56:34 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.006 |  |
| 2026-04-08 05:19:28 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.008 |  |
| 2026-04-08 05:09:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-04-08 05:10:40 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-08 02:07:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-08 05:01:05 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:02:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-08 05:03:23 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-08 05:03:33 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-08 05:01:56 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.022 |  |
| 2026-04-07 18:02:51 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-04-08 05:10:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.082 |  |
| 2026-04-08 05:03:40 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.113 |  |
| 2026-04-08 06:01:06 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.798 |  |
| 2026-04-08 06:00:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
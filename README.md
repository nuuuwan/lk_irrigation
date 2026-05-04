# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_02:35:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 02:35:13 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-05-05 02:14:43 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:11:59 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-05-05 02:10:38 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.112 |  |
| 2026-05-05 02:09:50 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-05 02:09:02 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.348 |  |
| 2026-05-05 02:08:03 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-05-05 02:06:39 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-05-05 02:06:28 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:06:16 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-05-05 02:06:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:05:31 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-05-05 02:05:03 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-05-05 02:05:02 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.003 |  |
| 2026-05-05 02:04:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:36 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:25 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-05 02:04:20 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-05 02:04:17 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:03:53 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.085 |  |
| 2026-05-05 02:03:32 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.142 |  |
| 2026-05-05 02:03:15 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:02:55 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -16.714 |  |
| 2026-05-05 02:02:36 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-05 02:02:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:02:27 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -16.714 |  |
| 2026-05-05 02:02:14 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:01:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:01:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-05 02:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 02:04:20 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-05 01:20:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-05 02:09:50 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-05 01:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-05 02:01:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-05 02:05:02 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.003 |  |
| 2026-05-05 02:01:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:34 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:00:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:02:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:14:43 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:03:15 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:17 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:06:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:02:14 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:36 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:04:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:06:28 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:06:16 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-05-05 02:05:03 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-05-05 02:04:25 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-05 02:02:36 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-05 02:35:13 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-05-05 02:08:03 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-05-05 02:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-05 02:05:31 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-05-05 02:11:59 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-05-05 02:06:39 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-05-05 02:03:53 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.085 |  |
| 2026-05-05 02:10:38 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.112 |  |
| 2026-05-05 02:03:32 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.142 |  |
| 2026-05-05 02:09:02 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.348 |  |
| 2026-05-05 02:02:55 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -16.714 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
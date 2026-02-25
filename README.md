# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_09:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,544 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 09:11:57 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-02-25 09:07:27 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:07:23 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:07:09 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:06:25 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:06:18 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:06:05 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:05:54 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:05:38 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-02-25 09:05:18 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:04:37 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.023 |  |
| 2026-02-25 09:04:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -2.348 |  |
| 2026-02-25 09:04:23 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-25 09:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 09:04:06 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:04:01 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:03:44 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -2.348 |  |
| 2026-02-25 09:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-25 09:03:08 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:03:04 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:02:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.098 |  |
| 2026-02-25 09:02:50 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:02:28 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 06:08:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-25 09:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-25 09:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 09:01:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:01:57 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:02:13 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:03:04 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:05:54 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:01:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:07:09 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:00:10 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:07:23 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:00:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:04:01 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:06:18 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:06:05 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:01:05 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:03:08 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:02:15 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:04:06 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:01:42 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:06:25 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:01:20 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:01:05 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-02-25 09:11:57 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-02-25 09:01:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.012 |  |
| 2026-02-25 09:07:27 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:02:50 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:05:18 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-02-25 09:05:38 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-02-25 09:04:37 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.023 |  |
| 2026-02-25 09:01:29 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-02-25 09:01:16 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-02-25 09:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.051 |  |
| 2026-02-25 09:04:23 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-25 09:02:28 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-02-25 09:02:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.098 |  |
| 2026-02-25 09:04:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -2.348 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
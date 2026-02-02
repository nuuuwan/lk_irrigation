# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_04:25:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,981 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 04:25:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-03 04:15:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:12:18 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-03 04:10:17 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-03 04:10:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:08:15 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-03 04:08:03 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 04:07:28 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-03 04:06:30 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -36.000 |  |
| 2026-02-03 04:06:29 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -36.000 |  |
| 2026-02-03 04:05:57 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-02-03 04:05:43 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-03 04:05:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:05:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:05:07 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.261 |  |
| 2026-02-03 04:04:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:04:39 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:04:38 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 04:03:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:03:30 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-02-03 04:03:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-02-03 04:02:19 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-03 04:02:15 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-02-03 04:02:12 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:02:10 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-03 04:01:43 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:16 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:14 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:09 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:00 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:00:47 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:00:37 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 03:56:29 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 03:01:05 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-02-03 04:05:57 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-02-03 04:08:15 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-03 04:25:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-03 04:05:43 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-03 04:10:17 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-03 03:56:29 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-03 04:02:19 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-03 04:04:38 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 04:07:28 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-03 04:12:18 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-03 04:04:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:14 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:05:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:02:10 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:03:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:04:39 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:05:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:02:12 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:16 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:00:47 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 03:05:48 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:09 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:15:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:01:00 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:00:37 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:10:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 04:08:03 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 04:01:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-03 04:03:30 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 04:02:15 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-02-03 04:03:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-02-03 03:04:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.035 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-03 04:05:07 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.261 |  |
| 2026-02-03 04:06:30 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
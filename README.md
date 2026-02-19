# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_20:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,578 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 20:12:32 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-02-19 20:11:22 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:09:27 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:53 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:30 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.106 |  |
| 2026-02-19 20:07:09 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:07 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:06:50 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 20:06:30 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-19 20:05:49 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-19 20:05:37 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:04:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:04:20 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-02-19 20:03:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 20:03:31 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:03:25 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-19 20:03:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:02:54 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:02:52 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 20:02:17 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-02-19 20:02:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:02:01 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:01:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-02-19 20:01:50 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-19 20:01:32 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:01:31 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-19 20:01:17 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:01:15 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:01:10 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.030 |  |
| 2026-02-19 20:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:00:10 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:58:39 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:55:00 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 20:04:20 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-02-19 20:01:31 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-19 20:03:25 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-19 20:05:49 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-19 20:01:50 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-19 20:06:30 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-19 19:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 20:03:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 20:02:52 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 20:06:50 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 20:00:10 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:10:43 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:04:28 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:03:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:02:01 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:07:50 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:04:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:12:34 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:09 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:09:27 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:03:31 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:05:37 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:07 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:11:22 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:07:53 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:01:15 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 20:02:54 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:02:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:01:32 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:01:17 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-19 20:12:32 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-02-19 20:01:10 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.030 |  |
| 2026-02-19 20:02:17 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-02-19 20:01:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-02-19 20:07:30 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
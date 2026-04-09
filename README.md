# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_04:11:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,934 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 04:11:24 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:10:56 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-10 04:08:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:07:51 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-10 04:07:12 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:06:24 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:05:12 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:04:08 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-04-10 04:03:26 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:09 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:02 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:02:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-04-10 04:02:43 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.120 |  |
| 2026-04-10 04:02:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -8.764 |  |
| 2026-04-10 04:01:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 04:01:45 | Holombuwa (Kelani Ganga) | 0.00 | 🟢 Normal | -0.130 |  |
| 2026-04-10 04:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:01:35 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 04:01:23 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-10 04:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:00:31 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:00:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:27:41 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.008 |  |
| 2026-04-10 03:22:02 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 04:02:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-04-10 04:01:23 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-10 02:12:28 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-10 04:10:56 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-10 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 03:02:31 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-10 04:01:35 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 04:01:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 04:00:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:10:12 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:02 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:26 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 02:05:58 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 02:01:24 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-04-10 02:05:33 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:11:24 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:00:31 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:02:09 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:08:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:09 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:03:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:06:24 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:07:12 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:08:07 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:09:30 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 01:52:00 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.005 |  |
| 2026-04-10 03:27:41 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.008 |  |
| 2026-04-10 04:07:51 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-10 03:16:02 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-04-10 03:04:16 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-10 04:04:08 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-10 04:02:43 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.120 |  |
| 2026-04-10 04:01:45 | Holombuwa (Kelani Ganga) | 0.00 | 🟢 Normal | -0.130 |  |
| 2026-04-10 04:02:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -8.764 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
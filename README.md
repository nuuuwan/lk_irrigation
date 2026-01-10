# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_20:15:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,080 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 20:15:46 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.046 |  |
| 2026-01-10 20:13:15 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:13:09 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:10:27 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:09:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-01-10 20:08:57 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:07:51 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-10 20:07:33 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:07:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-01-10 20:07:09 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:07:05 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 20:06:25 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 20:06:19 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.059 |  |
| 2026-01-10 20:05:33 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:05:22 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-01-10 20:04:32 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:03:43 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 2.601 | 🔺 Rising |
| 2026-01-10 20:03:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:03:16 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-10 20:02:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.033 |  |
| 2026-01-10 20:02:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:02:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:02:22 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:02:11 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-10 20:02:01 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:01:45 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:01:02 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:00:47 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:00:35 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-10 20:00:14 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:00:09 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 19:35:15 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 20:03:43 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 2.601 | 🔺 Rising |
| 2026-01-10 20:05:22 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-01-10 20:02:11 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-10 20:06:25 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 20:07:05 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 20:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-10 20:02:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:06:19 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:05:33 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 20:07:33 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:02:01 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:08:57 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:00:09 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 19:35:15 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:02:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:04:32 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:02:22 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:13:15 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:03:16 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:01:45 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:00:47 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:13:09 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:07:51 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-10 20:03:25 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:01:02 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:09:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:00:14 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:10:27 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-10 19:03:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-01-10 20:00:35 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 20:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-01-10 20:02:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.033 |  |
| 2026-01-10 20:15:46 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.046 |  |
| 2026-01-10 20:07:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2026-01-10 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
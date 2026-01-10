# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_02:45:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,286 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 02:45:07 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:24:12 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:23:11 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:22:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:12:15 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.127 |  |
| 2026-01-11 02:09:45 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:08:10 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.118 |  |
| 2026-01-11 02:07:13 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-11 02:06:17 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -1.000 |  |
| 2026-01-11 02:05:05 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -1.000 |  |
| 2026-01-11 02:04:55 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-11 02:04:38 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-01-11 02:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-11 02:03:36 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:03:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-01-11 02:03:02 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-11 02:03:00 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:02:52 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:02:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:02:19 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:58 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:39 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:35 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-11 02:01:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.005 |  |
| 2026-01-11 02:01:12 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:01:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:10 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 02:01:10 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:06 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:05 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:00:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:57:33 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 02:07:13 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-11 02:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-11 02:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-11 02:04:55 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-11 01:03:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 01:05:43 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 02:01:10 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 02:02:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:00:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:02:52 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:39 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:02:19 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:35 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:14:49 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:03:02 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:03:36 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:24:12 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:09:45 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:45:07 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:13:17 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:58 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:06 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:23:11 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:01:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.005 |  |
| 2026-01-11 01:57:33 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-01-11 02:03:00 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-11 00:04:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:01:12 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:01:05 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-01-11 02:04:38 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 02:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-11 02:03:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-01-11 02:08:10 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.118 |  |
| 2026-01-11 02:12:15 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.127 |  |
| 2026-01-11 02:06:17 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -1.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_17:19:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 17:19:32 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-11 17:10:59 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-11 17:10:55 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:09:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:08:58 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 17:08:20 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 17:08:19 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 17:07:40 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-11 17:07:37 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-11 17:07:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 17:07:21 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 17:06:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-06-11 17:05:42 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:05:31 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-11 17:05:07 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:04:54 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 17:04:52 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:04:29 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:04:26 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-11 17:04:25 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 17:04:09 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-06-11 17:03:50 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-11 17:03:48 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 17:03:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:03:26 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-11 17:02:54 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 17:06:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-06-11 17:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-06-11 17:04:26 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-11 17:03:26 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-11 17:03:50 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-11 17:05:31 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-11 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 17:10:59 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-11 17:07:40 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-11 17:08:58 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 17:03:48 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 17:07:21 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 17:02:54 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-11 17:04:54 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 17:00:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 17:08:19 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 17:04:25 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 17:07:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 17:08:20 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 17:19:32 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-11 17:04:29 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 15:03:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:05:07 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:03:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:10:55 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:00:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:02:02 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:05:42 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:01:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:02:18 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:00:50 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:04:52 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:00:29 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:09:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:01:25 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 17:07:37 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-11 17:01:11 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-06-11 17:04:09 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-06-11 17:01:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
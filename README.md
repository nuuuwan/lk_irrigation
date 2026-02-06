# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_20:42:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 20:42:17 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:15:56 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-02-06 20:12:42 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-06 20:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:09:44 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 20:08:58 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:08:24 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-02-06 20:07:54 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:07:51 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:07:40 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 20:07:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:05:20 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-06 20:04:49 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.088 |  |
| 2026-02-06 20:04:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-02-06 20:04:22 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:04:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:03:49 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-06 20:03:33 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.085 |  |
| 2026-02-06 20:03:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 20:02:53 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:50 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 20:02:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:38 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:29 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:28 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-06 20:02:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-02-06 20:02:10 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:43 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 20:01:33 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:32 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-06 20:01:28 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 20:15:56 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-02-06 20:03:49 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 20:01:43 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 20:03:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 20:05:20 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-06 20:12:42 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-06 20:01:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-06 20:02:50 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 20:07:40 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 20:09:44 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 20:02:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:33 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:08:58 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:04:22 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:38 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:42:17 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:53 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:32 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:07:51 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:07:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:04:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:07:54 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:29 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:01:28 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:10 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:28 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-06 20:04:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 20:02:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-02-06 20:08:24 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-02-06 20:03:33 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.085 |  |
| 2026-02-06 20:04:49 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
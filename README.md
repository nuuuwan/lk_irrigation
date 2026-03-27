# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_09:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 09:10:34 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 09:09:30 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:09:23 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:08:43 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-27 09:08:13 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.315 |  |
| 2026-03-27 09:07:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:07:47 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.036 |  |
| 2026-03-27 09:07:39 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-03-27 09:07:01 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:06:33 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:05:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:05:45 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:05:02 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:44 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:26 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:07 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.048 |  |
| 2026-03-27 09:04:05 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:03:23 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-27 09:02:49 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-03-27 09:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2026-03-27 09:02:34 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:06 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-27 09:02:00 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:52 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:01:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:38 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.042 |  |
| 2026-03-27 09:01:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:24 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:15 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:15 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:08 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-27 09:01:07 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:00:34 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 08:27:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.048 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 09:01:08 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-27 09:08:43 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-27 09:03:23 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-27 09:02:06 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-27 09:10:34 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 09:00:34 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 09:01:15 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:24 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:34 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:09:23 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:52 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:07 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:06:33 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:44 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:05:02 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:05:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:15 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:09:30 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:07:01 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:02:00 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:07:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:04:26 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 09:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:04:05 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:05:45 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-27 09:07:39 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-03-27 09:07:47 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.036 |  |
| 2026-03-27 09:02:49 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-03-27 09:01:38 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.042 |  |
| 2026-03-27 09:04:07 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.048 |  |
| 2026-03-27 09:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2026-03-27 09:08:13 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.315 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
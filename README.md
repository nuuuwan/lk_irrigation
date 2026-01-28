# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_09:14:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 09:14:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-28 09:10:13 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:09:12 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:09:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-01-28 09:07:49 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:07:48 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:07:02 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:05:41 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-01-28 09:05:28 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:05:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-28 09:05:05 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:04:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:04:32 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-01-28 09:04:26 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:03:55 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:03:42 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.071 |  |
| 2026-01-28 09:03:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-01-28 09:03:26 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.045 |  |
| 2026-01-28 09:03:22 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-28 09:03:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-28 09:02:52 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:47 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-28 09:02:44 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:38 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-01-28 09:02:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:19 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 09:02:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:01:38 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:01:20 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-01-28 09:01:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-01-28 09:01:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-01-28 09:01:19 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:00:29 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:00:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 09:01:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-01-28 09:02:47 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-28 09:03:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-28 09:03:22 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-28 09:14:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-28 09:05:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-28 09:02:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 09:00:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:44 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:03:55 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:07:48 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:10:13 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:07:49 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:07:02 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:05:28 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:02:38 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:09:12 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:04:26 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:05:05 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 09:04:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:19 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:01:38 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:01:19 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:00:29 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:02:52 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-28 09:01:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-01-28 09:05:41 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-01-28 09:04:32 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-01-28 09:01:20 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-01-28 09:03:26 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.045 |  |
| 2026-01-28 09:09:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-01-28 09:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-01-28 09:03:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-01-28 09:03:42 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_14:50:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 14:50:19 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:37:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.006 |  |
| 2025-12-31 14:14:58 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 14:12:58 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2025-12-31 14:09:56 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-31 14:09:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.125 |  |
| 2025-12-31 14:07:41 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2025-12-31 14:07:24 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.165 |  |
| 2025-12-31 14:07:11 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:06:01 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.023 |  |
| 2025-12-31 14:05:45 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-31 14:05:39 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:05:31 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:05:15 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2025-12-31 14:05:01 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2025-12-31 14:04:24 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:04:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:04:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 14:03:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:03:24 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:03:24 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:03:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 14:03:12 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:02:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-31 14:02:22 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:22 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:10 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:06 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:01:54 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:01:20 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:01:15 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.031 |  |
| 2025-12-31 14:01:14 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 14:00:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:53 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 14:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-31 14:04:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 14:09:56 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-31 14:01:14 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 14:03:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 14:14:58 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 14:02:22 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:22 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:04:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:10 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:05:39 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:07:11 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:50:19 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:01:20 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:02:06 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:03:24 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:00:53 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:04:24 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 14:37:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.006 |  |
| 2025-12-31 14:12:58 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2025-12-31 14:05:31 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:03:24 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:03:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:01:54 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:03:12 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-31 14:07:41 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2025-12-31 14:05:45 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-31 14:06:01 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.023 |  |
| 2025-12-31 14:01:15 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.031 |  |
| 2025-12-31 14:05:01 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2025-12-31 14:05:15 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2025-12-31 14:09:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.125 |  |
| 2025-12-31 14:07:24 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
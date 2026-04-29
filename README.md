# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_04:45:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 04:45:09 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:35:23 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 04:32:34 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 04:18:52 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-30 04:12:34 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:12:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.052 |  |
| 2026-04-30 04:09:21 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:08:56 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:08:00 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:06:59 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:06:33 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-30 04:06:02 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 04:04:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:04:23 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -2.769 |  |
| 2026-04-30 04:04:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-30 04:03:57 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -2.769 |  |
| 2026-04-30 04:03:47 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:03:39 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 04:03:39 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 04:03:38 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -2.769 |  |
| 2026-04-30 04:03:19 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 04:03:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:02:18 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.044 |  |
| 2026-04-30 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.113 |  |
| 2026-04-30 04:01:55 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 04:01:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 04:00:54 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.053 |  |
| 2026-04-30 04:00:40 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 04:00:25 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 04:03:39 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 04:03:39 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 04:03:19 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 02:18:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-30 04:01:55 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 03:01:50 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 04:32:34 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 04:18:52 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-30 04:06:02 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 04:35:23 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 04:01:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 04:00:40 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 02:03:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:09:21 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:12:34 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:04:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:08:00 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:03:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:06:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:06:59 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:42 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:04:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:08:56 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:45:09 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-30 04:06:33 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-30 03:34:06 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.013 |  |
| 2026-04-30 04:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-30 04:02:18 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.044 |  |
| 2026-04-30 03:04:07 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 04:12:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.052 |  |
| 2026-04-30 04:00:54 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.053 |  |
| 2026-04-30 03:03:00 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.057 |  |
| 2026-04-30 04:00:25 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.061 |  |
| 2026-04-30 01:07:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-30 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.113 |  |
| 2026-04-30 04:04:23 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_08:26:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 08:26:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:18:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:13:31 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:09:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:07:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-04-20 08:06:51 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.123 |  |
| 2026-04-20 08:06:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-04-20 08:06:27 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.090 |  |
| 2026-04-20 08:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.078 |  |
| 2026-04-20 08:06:15 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-04-20 08:06:09 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.086 |  |
| 2026-04-20 08:06:03 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-20 08:05:23 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:05:09 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:05:06 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-04-20 08:04:53 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-04-20 08:04:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-04-20 08:03:49 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:03:31 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-20 08:03:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:02:55 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:02:54 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-04-20 08:02:52 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:02:43 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.169 |  |
| 2026-04-20 08:02:42 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:02:31 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:02:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 08:02:08 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.119 |  |
| 2026-04-20 08:01:55 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-04-20 08:01:47 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:01:25 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-20 08:01:24 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 08:01:12 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.100 |  |
| 2026-04-20 08:00:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:00:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:00:23 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 08:06:03 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-20 08:03:31 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-20 08:01:24 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 08:02:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 08:00:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:05:23 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:18:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:05:09 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:00:23 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:03:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:09:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:13:31 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:01:47 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:02:52 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:26:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:03:49 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:09:56 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:02:31 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 08:07:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-04-20 08:02:42 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:02:55 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:00:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-20 08:02:54 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-04-20 08:01:25 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-20 08:06:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-04-20 08:05:06 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-04-20 08:01:55 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-04-20 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-20 08:04:53 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-04-20 08:06:15 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-04-20 08:04:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-04-20 08:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.078 |  |
| 2026-04-20 08:06:09 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.086 |  |
| 2026-04-20 08:06:27 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.090 |  |
| 2026-04-20 08:01:12 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.100 |  |
| 2026-04-20 08:02:08 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.119 |  |
| 2026-04-20 08:06:51 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.123 |  |
| 2026-04-20 08:02:43 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
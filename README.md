# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_06:16:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,344 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 06:16:45 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-02-16 06:15:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.095 |  |
| 2026-02-16 06:10:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:08:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:08:42 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:08:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-02-16 06:08:04 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.005 |  |
| 2026-02-16 06:08:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 06:07:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-02-16 06:06:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:06:18 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-02-16 06:06:11 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-16 06:05:47 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:45 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-02-16 06:05:40 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:32 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:31 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-02-16 06:05:07 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-02-16 06:04:38 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-16 06:04:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-02-16 06:04:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:03:34 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:02:57 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.053 |  |
| 2026-02-16 06:02:50 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-02-16 06:02:42 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.021 |  |
| 2026-02-16 06:02:12 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:56 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.002 |  |
| 2026-02-16 06:01:01 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 06:01:01 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:00:29 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:00:23 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-02-16 05:44:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:36:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 06:16:45 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-02-16 04:04:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 06:06:11 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-16 06:01:01 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 06:08:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 06:08:04 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.005 |  |
| 2026-02-16 06:01:01 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:02:12 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:56 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:08:42 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:32 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:03:34 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:04:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:40 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:08:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:05:47 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:00:29 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:10:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:06:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:44:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-16 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.002 |  |
| 2026-02-16 05:05:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.005 |  |
| 2026-02-16 06:04:38 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-16 06:05:45 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-02-16 06:05:31 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-02-16 06:00:23 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-02-16 06:05:07 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-02-16 06:02:42 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.021 |  |
| 2026-02-16 06:04:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-02-16 06:07:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-02-16 06:08:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-02-16 06:02:57 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.053 |  |
| 2026-02-16 06:15:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.095 |  |
| 2026-02-16 06:02:50 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
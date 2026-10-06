# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_16:09:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 16:09:03 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 16:08:05 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-06 16:07:34 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.039 |  |
| 2026-10-06 16:05:41 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-06 16:05:39 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.029 |  |
| 2026-10-06 16:05:28 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-06 16:04:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:04:22 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.102 |  |
| 2026-10-06 16:04:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-06 16:03:43 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.089 |  |
| 2026-10-06 16:03:30 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 16:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.53 | 🟢 Normal | -0.091 |  |
| 2026-10-06 16:03:19 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.050 |  |
| 2026-10-06 16:03:10 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.095 |  |
| 2026-10-06 16:02:49 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.050 |  |
| 2026-10-06 16:02:38 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-10-06 16:02:29 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:02:18 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-10-06 16:02:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:02:13 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.061 |  |
| 2026-10-06 16:02:12 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.071 |  |
| 2026-10-06 16:01:49 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-06 16:01:29 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:25 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-06 16:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 16:00:55 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:00:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 16:00:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 16:02:38 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-10-06 16:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 16:03:30 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 16:00:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 16:09:03 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:00:55 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:02:29 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:25 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:03:12 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:44 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:04:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:02:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:01:29 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:05:41 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-06 16:01:49 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-06 16:01:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:01:16 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-10-06 16:08:05 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-06 16:00:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-06 16:05:39 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.029 |  |
| 2026-10-06 16:05:28 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-06 16:02:18 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-10-06 16:07:34 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:03:07 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:05:08 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.045 |  |
| 2026-10-06 16:03:19 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.050 |  |
| 2026-10-06 16:02:49 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.050 |  |
| 2026-10-06 16:02:13 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.061 |  |
| 2026-10-06 16:04:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-06 16:02:12 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.071 |  |
| 2026-10-06 16:03:43 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.089 |  |
| 2026-10-06 16:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.53 | 🟢 Normal | -0.091 |  |
| 2026-10-06 16:03:10 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.095 |  |
| 2026-10-06 16:04:22 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)